@echo off
echo Setting up House Price Predictor project...

:: Create main project directory
set PROJECT_DIR=house-price-predictor
mkdir %PROJECT_DIR%
cd %PROJECT_DIR%

:: Create required folders
mkdir .github\workflows
mkdir model
mkdir app\templates
mkdir app\static
mkdir tests

:: Create empty files
echo. > .gitignore
echo. > README.md
echo. > model\train_model.py
echo. > model\model.pkl
echo. > model\locations.pkl
echo. > model\columns.pkl
echo. > app\app.py
echo. > app\requirements.txt
echo. > app\templates\index.html
echo. > tests\test_api.py
echo. > .github\workflows\deploy.yml

echo Project structure created successfully!
pause
