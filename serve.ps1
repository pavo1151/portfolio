# Amit Ozan studio: a tiny local web server, no installation needed (Windows PowerShell 5+).
# Browsers block 3D textures and modules on pages opened as file://, so the site is served on http://localhost.
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$types = @{ '.html'='text/html; charset=utf-8'; '.js'='text/javascript; charset=utf-8'; '.css'='text/css; charset=utf-8';
  '.jpg'='image/jpeg'; '.jpeg'='image/jpeg'; '.png'='image/png'; '.svg'='image/svg+xml'; '.webp'='image/webp';
  '.mp4'='video/mp4'; '.woff2'='font/woff2'; '.json'='application/json'; '.txt'='text/plain; charset=utf-8' }
$listener = $null; $port = 0
foreach ($p in 8765..8785) {
  try { $l = New-Object System.Net.HttpListener; $l.Prefixes.Add("http://localhost:$p/"); $l.Start(); $listener = $l; $port = $p; break } catch { }
}
if (-not $listener) { Write-Host 'No free port between 8765 and 8785.'; Read-Host 'Press Enter to close'; exit 1 }
$url = "http://localhost:$port/"
Write-Host ''
Write-Host "  The site is running at $url"
Write-Host '  Keep this window open while you browse. Close it to stop the site.'
Write-Host ''
Start-Process $url
$rootFull = [System.IO.Path]::GetFullPath($root)
while ($listener.IsListening) {
  try {
    $ctx = $listener.GetContext(); $req = $ctx.Request; $res = $ctx.Response
    $rel = [Uri]::UnescapeDataString($req.Url.AbsolutePath).TrimStart('/')
    if ($rel -eq '' -or $rel.EndsWith('/')) { $rel = $rel + 'index.html' }
    $full = [System.IO.Path]::GetFullPath((Join-Path $rootFull $rel))
    if (-not $full.StartsWith($rootFull) -or -not (Test-Path -LiteralPath $full -PathType Leaf)) {
      $res.StatusCode = 404; $b = [Text.Encoding]::UTF8.GetBytes('Not found'); $res.OutputStream.Write($b, 0, $b.Length); $res.Close(); continue
    }
    $ext = [System.IO.Path]::GetExtension($full).ToLower()
    $res.ContentType = $(if ($types.ContainsKey($ext)) { $types[$ext] } else { 'application/octet-stream' })
    $res.AddHeader('Accept-Ranges', 'bytes'); $res.AddHeader('Cache-Control', 'no-cache')
    $bytes = [System.IO.File]::ReadAllBytes($full); $start = 0; $end = $bytes.Length - 1
    $range = $req.Headers['Range']
    if ($range -and $range -match 'bytes=(\d*)-(\d*)') {
      if ($matches[1] -ne '') { $start = [int64]$matches[1] }
      if ($matches[2] -ne '') { $end = [Math]::Min([int64]$matches[2], $bytes.Length - 1) }
      $res.StatusCode = 206; $res.AddHeader('Content-Range', "bytes $start-$end/$($bytes.Length)")
    }
    $len = $end - $start + 1; $res.ContentLength64 = $len
    if ($req.HttpMethod -ne 'HEAD') { $res.OutputStream.Write($bytes, [int]$start, [int]$len) }
    $res.Close()
  } catch { try { $res.Abort() } catch { } }
}
