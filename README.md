# INF8808 Project – Data Visualization

This project is built with **Dash** and **Plotly**, designed for visualizing and exploring Spotify song data.

## 📁 Project Structure

```

DataViz/
    ├── code/
    │   └── src/             # Contains all application source code
    │       ├── app.py
    │       ├── server.py
    │       ├── scatter_chart.py
    │       ├── ...
    │       └── requirements.txt
    ├── requirements.windows.txt
    ├── requirements.linux.txt
    └── README.md            # This file
```

## 🚀 Deployment (Render)

The app is deployed using [Render](https://render.com). The working directory is set to `code/src`, and the build/start commands are:

- **Build Command**:  
  ```bash
  pip install -r requirements.txt
  ```

- **Start Command**:  
  ```bash
  gunicorn app:server
  ```

##  Local Development

To run the app locally:

```bash
cd code/src
pip install -r requirements.txt  # Or use requirements.windows.txt if you're on Windows
python server.py
```

The app will be accessible at:  
📍 `http://localhost:8050`

##  Requirements

Main dependencies include:

- Dash
- Plotly
- Pandas
- Flask
- Gunicorn

OS-specific dependencies:
- `colorama` for Windows
- Use `requirements.linux.txt` for Linux environments

## 📊 Features

- Interactive charts using Dash components
- Filtered visualizations of Spotify track features
- Responsive layout with Bootstrap components

## 📌 Notes

- The working directory for deployment is `code/src`.
- `requirements.windows.txt` and `requirements.linux.txt` contain complete environment configurations.
- `requirements.txt` is used for production deployment.
