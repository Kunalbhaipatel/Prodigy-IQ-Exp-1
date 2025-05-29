
# Prodigy IQ Shaker Cost Comparison Dashboard

This is a professional Streamlit application built for **comparing flowline shaker costs** across different well setups using real operational data. It includes:

- Dynamic filters by shaker model, operator, contractor, and well
- Cost estimation toggles for dilution, haul-off, equipment, screens, and more
- Visual image preview of selected shaker
- Real-time savings comparison (Derrick vs Non-Derrick)

---

## 📁 Project Structure

```
.
├── app.py                    # Main Streamlit entry point
├── dual_filter_panel.py     # Dual column filter + config toggles
├── shaker_image_map.py      # Model-to-image mapping
├── Refine Sample.csv        # Drilling dataset
├── requirements.txt         # Python dependencies
└── images/                  # Shaker equipment images
```

---

## 🚀 How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Start the App
```bash
streamlit run app.py
```

---

## 🌐 Features

- 📸 Image preview of shaker models
- 🔄 Dynamic filters based on selected shaker
- 📊 Cost breakdown comparison between Derrick vs Non-Derrick units
- 💡 Designed for operations, engineering, and sales teams

---

## 📦 Deployment Ready
You can deploy this app to:
- [Streamlit Cloud](https://share.streamlit.io)
- Azure App Services
- GitHub Pages (static docs or instructions)

---

## 🧠 Powered by Prodigy IQ
Built to help drilling teams make faster, data-driven decisions on shaker efficiency and savings.

