# Global Energy Consumption

ML model that predicts global energy consumption using libraries- i)Numpy ii)Pandas iii)Scikit learn iv)Matplotlib

`AI101 Mini-Project` · `Group 73` · `Python 3.10+`

---

## Team and roles

| Member | Entry no. | Role |
|--------|-----------|------|
| Aadyant Chaturvedi | 2026EEB1311 | Documentation Lead |
| Ayush Yogesh Sakure | 2026AIB1026 | Execution Lead |
| Padakandla Rohith | 2026MCB1552 | Video Lead |
| Sahil Shekhawat | 2026EEB1405 | PPT Lead |

*All members contributed code (see commit history).*

---

## Project structure

```
Predicting-Global-Energy-Consumption/
├── Dataset/
│   └── dataset_Description.md
│   └── global_energy_consumption.csv
├── Source/
│   ├── main.py
├── requirements.txt
└── README.md
```

---

## Dataset

| Item | Details |
|------|---------|
| Source | [https://www.kaggle.com/datasets/atharvasoundankar/global-energy-consumption-2000-2024] |
| Licence / terms of use | CC0: Public Domain |
| Rows × columns | 10001x10 |
| Time period covered | 2000-2024 |
| Geographic coverage | Australia, Brazil, China, Canada, Germany, India, Japan, Russia, UK, USA |
| Consumption measured | Global Energy Consumption in TWh |
| Target variable | Global Energy Consumption in TWh |
| Features used | Year, Per Capita Energy Use(kWh), Renewable Energy Share(%), Fossil Fuel Dependency(%), Industrial Energy Use(%), Household Energy Use(%), Carbon Emissions Index (Million Tons), Energy Price Index (USD/kWh) |
| Preprocessing | Clean Dataset, Train-Test Split performed (random_state=42, test_size=0.2), Since its a linear regression model --> no scaling is required|

---

## Method

| Item | Details |
|------|---------|
| Problem type | Regression |
| Model(s) | Linear Regression |
| Train / test split | test_size=0.2,random_state=42 |
| Evaluation metric(s) | MAE,RMSE,Precision,Recall,Accuracy,F1 score |
| Results | (To be updated) |

---

## Setup

Tested on Python 3.15.0 (Windows 11,10).

```bash
git clone https://github.com/Aadyant-Chaturvedi/Predicting-Global-Energy-Consumption/edit/main/README.md
cd Predicting-Global-Energy-Consumption
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Download Dataset from https://www.kaggle.com/datasets/atharvasoundankar/global-energy-consumption-2000-2024

---

## How to run (to be updated)

1. [Exact command, e.g. `python [path/to/script]`]
2. [What the script prints or saves, and where]
3. Expected runtime: approximately [time] on [hardware]

---

## Expected output

[Insert a screenshot of the terminal output.]

![Terminal output]([path/to/screenshot])

[Insert screenshots of any saved plots, with a one-line caption for each.]

![[Plot description]]([path/to/plot])

---

## Links

- Slides ([number] min): [link or path]
- Video ([length]): [link]

---

## AI-use disclosure

(To be updated)
