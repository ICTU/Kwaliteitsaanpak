<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:outline="http://wkhtmltopdf.org/outline"
                xmlns="http://www.w3.org/1999/xhtml">
  <xsl:output doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"
              doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"
              indent="yes" />
  <xsl:template match="outline:outline">
    <html>
      <head>
        <title>Inhoudsopgave</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style>
          @import url("/ka/DocumentDefinitions/Shared/cover.css");
          div {border-bottom: 1px dashed rgb(200,200,200);}  /* dashed line to connect titles and page numbers */
          span {float: right;}  /* right align page number */
          li {list-style: none;}  /* no bullets */
          ul {font-size: 14pt; padding-left: 0em;}
          ul ul {font-size: 80%; padding-left: 1em;}  /* indent subsections and use smaller font */
          ul ul ul {display: none;}  /* don't display subsubsections, works recursively */
          a {text-decoration:none; color: inherit;}  /* don't render links blue/underlined */
        </style>
      </head>
      <body>
        <h2>Inhoudsopgave</h2>
        <ul><xsl:apply-templates select="outline:item/outline:item"/></ul>
      </body>
    </html>
  </xsl:template>
  <xsl:template match="outline:item">
    <li>
      <xsl:if test="(@title!='') and (@title!='Inhoudsopgave')">
        <div>
          <a>
            <xsl:if test="@link">
              <xsl:attribute name="href"><xsl:value-of select="@link"/></xsl:attribute>
            </xsl:if>
            <xsl:if test="@backLink">
              <xsl:attribute name="name"><xsl:value-of select="@backLink"/></xsl:attribute>
            </xsl:if>
            <xsl:variable name="depth" select="count(ancestor::*)"/>
            <xsl:if test="$depth = 2">
              <xsl:value-of select="concat(position()-1, ' ', @title)"/>
            </xsl:if>
            <xsl:if test="$depth > 2">
              <xsl:value-of select="concat(position(), ' ', @title)"/>
            </xsl:if>
          </a>
          <span> <xsl:value-of select="@page" /> </span>
        </div>
      </xsl:if>
      <ul>
        <xsl:comment>added to prevent self-closing tags in QtXmlPatterns</xsl:comment>
        <xsl:apply-templates select="outline:item"/>
      </ul>
    </li>
  </xsl:template>
</xsl:stylesheet>
