import sys
import logging
from vogue.build.application_tag import build_application_tag
LOG = logging.getLogger(__name__)
   

def load_aplication_tags(adapter, db_json_list, dry_run=False):
    """Will go through all application tags in db_json_list and add/update them to trending-db."""
    
    if dry_run:
        LOG.info("Will go through all application tags in db_json_list and add/update them in trending-db.")
        return

    for application_tag in db_json_list:
        mongo_application_tag = build_application_tag(application_tag)
        if isinstance(mongo_application_tag, dict):
            adapter.add_or_update_application_tag(mongo_application_tag)
