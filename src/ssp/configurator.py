from functools import wraps
import inspect
from typing import get_type_hints


def resolve_dependencies(cls, registry):
    """
    Recursively instantiate dependencies for a class with type-annotated __init__, using registry.
    """
    sig = inspect.signature(cls.__init__)
    params = list(sig.parameters.items())[1:]  # skip 'self'
    dep_args = []
    for name, param in params:
        if param.annotation is inspect.Parameter.empty:
            raise TypeError(f"Missing type annotation for parameter '{name}' in '{cls.__name__}'")
        dep_type = param.annotation
        dep_impl = registry.get(dep_type)
        if dep_impl is None:
            # Try direct type
            dep_impl = registry.get(name)  # fallback: try by param name
        if dep_impl is None:
            raise ValueError(f"No implementation found in registry for {dep_type} ('{name}')")
        if inspect.isclass(dep_impl):
            # Recursively resolve dependencies if adapter has typed constructor
            try:
                sub_sig = inspect.signature(dep_impl.__init__)
                # More than just self?
                if len(sub_sig.parameters) > 1:
                    dep_obj = resolve_dependencies(dep_impl, registry)
                else:
                    dep_obj = dep_impl()
            except Exception:
                dep_obj = dep_impl()
        else:
            dep_obj = dep_impl
        dep_args.append(dep_obj)
    return cls(*dep_args)


def configurator(registry=None):
    """
    Decorator that injects dependencies based on handler and service type annotations.
    `registry` should be a dict mapping port types (interfaces) to concrete implementations
    """
    registry = registry or {}

    def decorator(fn):
        @wraps(fn)
        def wrapper(event, context, *args, **kwargs):
            hints = get_type_hints(fn)
            service_type = hints.get("service")
            if service_type is None:
                raise TypeError("Handler function must have a type-annotated 'service' parameter for injection")

            service_instance = resolve_dependencies(service_type, registry)
            return fn(event, context, service_instance, *args, **kwargs)
        return wrapper
    return decorator
