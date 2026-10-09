$ErrorActionPreference = "Stop"
$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
    throw "Project Python environment not found. Create it with: py -m venv .venv"
}
& $python (Join-Path $PSScriptRoot "main.py")
exit $LASTEXITCODE
