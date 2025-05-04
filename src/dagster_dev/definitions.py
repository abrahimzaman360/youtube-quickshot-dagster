import dagster_dev.defs
from dagster.components import definitions, load_defs


@definitions
def defs():
    return load_defs(defs_root=dagster_dev.defs)
        
