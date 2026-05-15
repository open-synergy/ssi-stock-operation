import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-stock-operation",
    description="Meta package for open-synergy-ssi-stock-operation Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_stock_picking_type_category',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
