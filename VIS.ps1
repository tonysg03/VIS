$filename = Get-ChildItem ".\VIS\Paises\*\*.isl" -Recurse

$previous_user = "asegura"

$filename | %{
    (gc $_) -replace "$previous_user","$env:UserName" |Set-Content $_.fullname
}

if ([System.IO.File]::Exists('$home\Desktop')){
    $filename | %{
    (gc $_) -replace "Escritorio","Desktop" |Set-Content $_.fullname
    }
} else {
    $filename | %{
    (gc $_) -replace "Desktop","Escritorio" |Set-Content $_.fullname
    }
}

$filenamePY = Get-ChildItem ".\VIS\Codigo\VIS.py" -Recurse

if ([System.IO.File]::Exists('$home\Desktop')){
    $filenamePY | %{
    (gc $_) -replace "Escritorio","Desktop" |Set-Content $_.fullname
    }
} else {
    $filenamePY | %{
    (gc $_) -replace "Desktop","Escritorio" |Set-Content $_.fullname
    }
}