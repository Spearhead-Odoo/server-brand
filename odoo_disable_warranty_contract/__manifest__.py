{
    "name": "Odoo disable warranty contract",
    "summary": "Odoo disable warranty contract",
    "version": "17.0.1.0.0",
    "author": "Spearhead, Carlos Lopez",
    "website": "https://github.com/OCA/server-brand",
    "category": "Tools",
    "license": "AGPL-3",
    "depends": [
        "base",
        "web_enterprise",
    ],
    "assets": {
        "web.assets_backend": [
            "odoo_disable_warranty_contract/static/src/webclient/**/*.js",
        ],
    },
    "installable": True,
}
