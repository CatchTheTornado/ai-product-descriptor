## AI Product Descriptor

This is an PoC of a REST service extracting product text description and structuralized attributes from product image. 

Potential use cases:
- automate product description for eCommerce and PIM's,
- visual search engines,
- ...

## Example usage

**Input:**
<img src="https://upload.wikimedia.org/wikipedia/commons/4/49/Sports_shoes.jpg" />

**Output:**

```json
{
    "description": "Unleash your style with these **iconic sports-inspired sneakers**. Crafted for comfort and designed for an active lifestyle, these sneakers feature a sleek, **low-top silhouette** with a durable **white and silver mesh upper with synthetic overlays** for breathability and support. Accented by **signature swoosh logos** in a contrasting black, this pair adds an edgy pop to your outfits. Secure your fit with **black laces** atop a classic lace-up closure. A padded **red collar** provides extra ankle support, while the soft fabric lining ensures a comfortable in-shoe feel. Built to last, the **rubber outsole with a traction pattern** enhances grip, and a visible **air cushioning unit** in the heel absorbs impact. These sneakers are a perfect blend of style, performance, and comfort, making them suitable for both athletic activities and casual wear.",
    "attributes": [
        {
            "category": "Footwear"
        },
        {
            "style": "Sports Sneaker"
        },
        {
            "color": "White/Silver with Red and Black accents"
        },
        {
            "closure_type": "Lace-up"
        },
        {
            "material_upper": "Mesh with Synthetic Overlays"
        },
        {
            "logo": "Swoosh"
        },
        {
            "collar_type": "Padded"
        },
        {
            "lining_material": "Fabric"
        },
        {
            "sole_material": "Rubber"
        },
        {
            "cushioning": "Visible Air Unit"
        },
        {
            "pattern": "Traction"
        },
        {
            "gender": "Unisex"
        },
        {
            "size": "Not specified"
        },
        {
            "condition": "New"
        }
    ]
}
```


## Getting Started

This guide will walk you through the process of checking out and setting up the project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Python 3.6+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Installation

1. **Clone the Repository**

   First, clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/yourusername/your_project_name.git
   cd your_project_name

2. **Create a Virtual Environment (Optional but Recommended)**

   It's a good practice to create a virtual environment for your Python projects. Use the following commands to create and activate one:

   - For Unix or MacOS:

     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

   - For Windows:

     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```

3. **Install Dependencies**

   Install the required packages using:

   ```bash
   pip install -r requirements.txt
   ```

4. **Running the Application**

   To run the application please do use

   ```bash
   export OPENAI_API_KEY={your API key from platform.chatgpt.com}
   uvicorn app.main:app --reload
  
   ```

## TODO

1. Add async call support.
2. Authorization support
3. ...
