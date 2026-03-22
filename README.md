# drink_quality_prediction

***

# Drinks Quality Prediction System 🥤

A machine learning pipeline to predict drink quality using advanced ML techniques. Built with Python 3.8, Docker support, and modular configuration management.

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
```

## 🐳 Docker Deployment

```bash
# Build and run with Docker
docker build -t drinks-quality-prediction .
docker run -p 8080:8080 drinks-quality-prediction
```

## 🏗️ Project Structure & Development Workflow

```
📁 src/
├── config/           # Configuration management
├── components/       # ML pipeline components
├── entity/          # Data classes & schemas
├── pipeline/        # Main ML pipeline
└── utils/           # Helper utilities

📄 config files:
├── config.yaml      # Main configuration
├── schema.yaml      # Data validation schema  
├── params.yaml      # Hyperparameters
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

- **Modular ML Pipeline**: Config-driven training & prediction
- **Data Validation**: YAML-based schema validation
- **Dockerized**: One-command deployment
- **Config Management**: Separate params for easy experimentation
- **Scalable**: Component-based architecture

## 📊 ML Pipeline Stages

```
Raw Data → Data Validation → Data Transformation → 
Model Training → Model Evaluation → Prediction API
```

## 💻 Tech Stack

```
🐍 Python 3.8 | Docker | Conda
🤖 ML: Scikit-learn/PyTorch | Pipeline orchestration
📊 Config: YAML | Data: Pandas
🌐 API: FastAPI/Flask
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

***

**Built for ML production deployment** | **bhilwara, Rajasthan** | **March 2026**



ecr uri  ->   904871342857.dkr.ecr.us-east-1.amazonaws.com/drinkrepo