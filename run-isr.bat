call node_modules\.bin\markdown-include.cmd .\DocumentDefinitions\ISR\document.json
call node_modules\.bin\markdown.cmd ICTU-Kwaliteitsaanpak-ISR.md -s %cd%/DocumentDefinitions/ISR/document.css > ICTU-Kwaliteitsaanpak-ISR.html
call node htmltopdf.js ICTU-Kwaliteitsaanpak-ISR.html
