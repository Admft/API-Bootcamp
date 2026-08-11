# One-Day Setup (Windows PowerShell)
# Run from the project root: .\setup.ps1

Write-Host "=== One-Day API Integration Lab ===" -ForegroundColor Cyan

# Create virtual environment
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# Activate and install
Write-Host "Installing dependencies..."
& .\venv\Scripts\pip.exe install -r requirements.txt -q

# Copy .env if missing
if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "Created .env from .env.example"
}

Write-Host ""
Write-Host "Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Activate:  .\venv\Scripts\Activate.ps1"
Write-Host "  3. Start course: python course\app.py  →  http://127.0.0.1:8080"
Write-Host "  4. Start APIs:   python mock-apis\run_servers.py"
Write-Host ""
