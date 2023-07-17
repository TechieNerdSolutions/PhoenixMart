# PhoenixMart

PhoenixMart eCommerce platform is built with Django, offering a comprehensive solution for online marketplace needs. It provides a feature-rich environment for both Vendors and users, facilitating the buying and selling of products in various categories.

![PhoenixMart](./static/assets/imgs/phoenix.png)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Bug Reports and Feature Requests](#bug-reports-and-feature-requests)
- [Code of Conduct](#code-of-conduct)
- [License](#license)




## Features

- User authentication and registration
- User roles: Vendor and Buyer
- Vendor dashboard for managing products, orders, and inventory
- Product listing with details, images, and pricing
- Category-based product organization
- Advanced search functionality
- Shopping cart and order placement
- Multiple payment options (e.g., Stripe, PayPal)
- Order tracking and status updates
- Wishlist feature for users
- Reviews and ratings for products
- Admin panel for site management

## Installation

To run PhoenixMart locally, ensure you have Python and Django installed on your system. Follow these steps to install and run the project:

1. Clone this repository:

```bash
git clone https://github.com/TNSQUAD/PhoenixMart.git
```

2. Navigate to the project directory:

```bash
cd PhoenixMart
```

3. Create a virtual environment:

```bash
python -m venv env
```

4. Activate the virtual environment:
   - ```bash
     source env/bin/activate # Unix/Linux
     ```
     <p align="center"><strong>OR</strong></p>
   - ```bash
      env\Scripts\activate (Windows)
     ```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Set up the database:

```bash
python manage.py migrate
```

7. Create a superuser:

```bash
python manage.py createsuperuser
```

8. Run the development server:

```bash
python manage.py runserver
```

9. Access the website in your browser at `http://localhost:8000`.

## Usage

- Visit the [homepage](https://pheonixmart.onrender.com) to explore the marketplace and browse products by category.
- Sign up or log in...
  - **As a buyer**: to add products to your cart, place orders, and manage your profile.
  - **As a vendor**: to access the Vendor dashboard, where you can manage your products, inventory, and orders.
- Use the search functionality to find specific products by name, category, or keywords.
- Admins can access the admin panel at ```/admin``` to manage site settings, categories, and user accounts.
- For more information please refer to this [documentation](docs/documentation.md)

## Contributing

Please see the [Contributor's Guide](CONTRIBUTING.md) for details on how to contribute to PhoenixMart. We welcome bug reports, feature requests, and code contributions.

## Bug Reports and Feature Requests

If you encounter any bugs or have suggestions for new features, please submit an issue on the [issue tracker](.github/issues.md).
-  [Issue Tracker](.github/issues.md)
-  [Document Update](.github/doc_update.md)
-  [Feature Request](.github/feature_request.md)
-  [Design Report](.github/design_report.md)
-  [For Any Question](.github/question.md)
We appreciate detailed bug reports and clear feature requests.

## Code of Conduct

We enforce a [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and respectful community for all contributors. Please make sure to review and adhere to it.

## License

This project is licensed under the [MIT License](LICENSE).
