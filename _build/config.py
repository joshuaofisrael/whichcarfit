"""Single site switches. Canonical host is always whichcarfit.com.

NOINDEX is the one flag that keeps every page out of search until the domain
is the live host. Set it to False only for the launch build.
"""
NOINDEX = True
BASE_URL = "https://whichcarfit.com/"
BRAND = "Which Car Fit"
DOMAIN = "whichcarfit.com"
PUBLISHED = "2026-11-16"
PUBLISHED_H = "16 Nov 2026"
INDEXNOW_KEY = "15cffb11329a506a716afdc6f6099cae"
# Shared JI Ventures Analytics 2 token, same family as the sister sites.
# Written into pages only when NOINDEX is False.
CF_BEACON_TOKEN = "eac63f2b5dbc4539a2d95249baab6472"
CONTACT_EMAIL = "joshuaofisrael@gmail.com"
LEGAL_LINE = (
    "© 2026 Joshua Israel Ventures LLC. All rights reserved. "
    "Which Car Fit is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company."
)
