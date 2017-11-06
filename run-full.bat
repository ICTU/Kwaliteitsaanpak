call node_modules\.bin\markdown-include.cmd .\DocumentDefinitions\Full\document.json
call node_modules\.bin\markdown.cmd ICTU-Kwaliteitsaanpak-Full.md -s %cd%/DocumentDefinitions/Full/document.css > ICTU-Kwaliteitsaanpak-Full.html
call node htmltopdf.js ICTU-Kwaliteitsaanpak-Full.html
