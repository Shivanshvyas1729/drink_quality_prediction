
````md
# drink_quality_prediction
```md
Built with Python 3.10, Docker support, modular configuration management, and CI/CD pipeline integration using GitHub Actions, AWS ECR, and AWS EC2.
````
live --> https://drinkqualityprediction.streamlit.app/

***

# Drinks Quality Prediction System 🥤

A machine learning pipeline to predict drink quality using advanced ML techniques. Built with Python 3.10, Docker support, modular configuration management, and a complete CI/CD deployment workflow using GitHub Actions, AWS ECR, and AWS EC2.

## 🚀 Quick Start

```bash
# 1. Create virtual environment
conda create -n mlproj python=3.10 -y

# 2. Activate environment
conda activate mlproj

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
````

## 🐳 Docker Deployment

```bash
# Build and run with Docker
docker build -t drinks-quality-prediction .
docker run -p 8080:8080 drinks-quality-prediction
```

## 🔄 CI/CD Deployment Pipeline

This project includes a complete CI/CD pipeline for automated deployment.

### CI/CD Workflow

* **GitHub Actions** is used to automate build and deployment
* **Docker image** is built automatically on code push
* The image is pushed to **AWS Elastic Container Registry (ECR)**
* The application is deployed on an **AWS EC2 instance**
* This setup enables fast, consistent, and production-ready deployments

### Deployment Stack

* **GitHub Actions** – CI/CD automation
* **AWS ECR** – Docker image storage
* **AWS EC2** – Application hosting

> ECR Repository: `904871342857.dkr.ecr.us-east-1.amazonaws.com/drinkrepo`

## 🏗️ Project Structure & Development Workflow

```bash
📁 src/
├── config/           # Configuration management
├── components/       # ML pipeline components
├── entity/           # Data classes & schemas
├── pipeline/         # Main ML pipeline
└── utils/            # Helper utilities

📄 config files:
├── config.yaml       # Main configuration
├── schema.yaml       # Data validation schema
├── params.yaml       # Hyperparameters
```

### Development Workflow

1. **Update `config.yaml`** - Modify experiment settings
2. **Update `schema.yaml`** - Change data validation rules
3. **Update `params.yaml`** - Tune hyperparameters
4. **Update entities** in `src/entity/`
5. **Update config manager** in `src/config/`
6. **Update components** in `src/components/`
7. **Update pipeline** in `src/pipeline/`
8. **Update `main.py`** - Experiment runner
9. **Update `app.py`** - Production API

## 🔧 Key Features

* **Modular ML Pipeline**: Config-driven training & prediction
* **Data Validation**: YAML-based schema validation
* **Dockerized Deployment**: Container-based packaging
* **CI/CD Integration**: Automated deployment with GitHub Actions
* **AWS Deployment**: Image storage in ECR and hosting on EC2
* **Config Management**: Separate params for easy experimentation
* **Scalable Architecture**: Component-based project structure

## 📊 ML Pipeline Stages

```bash
Raw Data → Data Validation → Data Transformation → 
Model Training → Model Evaluation → Prediction API → Deployment
```

## 💻 Tech Stack

```bash
🐍 Python 3.10 | Docker | Conda
🤖 ML: Scikit-learn / PyTorch
📊 Config: YAML | Data: Pandas
🌐 App: Streamlit
☁️ Cloud: AWS ECR, AWS EC2
🔄 CI/CD: GitHub Actions
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

## 🙌 Support

Star ⭐ the repo if this helps you! Questions? Open an issue.

---

**Built for ML production deployment** | **Bhilwara, Rajasthan** | **March 2026**

````





I can also turn this into a more polished, recruiter-friendly README version.
