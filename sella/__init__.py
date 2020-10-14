from .optimize import IRC, Sella
from jax.config import config

config.update("jax_enable_x64", True)

__all__ = ['IRC', 'Sella']
