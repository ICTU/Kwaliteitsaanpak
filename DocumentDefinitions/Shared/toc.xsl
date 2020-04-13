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
          @import url("/work/DocumentDefinitions/Shared/cover.css");
          div {
            border-bottom: 1px solid #AFAFAF;
          }
          span.chapter-number {
            padding-right: 0.6em;
            color: #4C76BA;  /* Blue */
          }
          span.section-number {
            padding-right: 0.6em;
            color: #6F6F6F;  /* Grey */
          }
          span.chapter-page-number {
            float: right;  /* Right align page number */
            color: #4C76BA;  /* Blue */
          }
          span.section-page-number {
            float: right;  /* Right align page number */
            color: #6F6F6F;  /* Grey */
          }
          ul {
            font-size: 12pt;
            font-weight: bold;
            padding-left: 0em;
            line-height: 200%;
          }
          ul ul {
            padding-left: 1.6em;  /* Indent subsections */
            font-weight: normal;
            line-height: 175%;
          }
          ul ul ul {display: none;}  /* Don't display subsubsections, works recursively */
          li {list-style: none;}  /* No bullets */
          a {text-decoration:none; color: inherit;}  /* Don't render links blue/underlined */
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
          <xsl:variable name="depth" select="count(ancestor::*)"/>
            <xsl:if test="($depth = 2) and (@title!='Bijlagen')">
              <span class="chapter-number">
                <xsl:value-of select="concat(position()-1, ' ')"/>
              </span>
            </xsl:if>
            <xsl:if test="$depth > 2">
              <span class="section-number">
                <xsl:if test="../@title!='Bijlagen'">
                  <xsl:value-of select="concat(count(parent::*/preceding-sibling::*) + 1, '.', position(), ' ')"/>
                </xsl:if>
                <xsl:if test="../@title='Bijlagen'">
                  <xsl:variable name="alphapos" select="substring('ABCDEFGHIJKLMNOPQRSTUVWXYZ', position(), 1)"/>
                  <xsl:value-of select="concat($alphapos, ' ')"/>
                </xsl:if>
              </span>
            </xsl:if>
          <a>
            <xsl:if test="@link">
              <xsl:attribute name="href"><xsl:value-of select="@link"/></xsl:attribute>
            </xsl:if>
            <xsl:if test="@backLink">
              <xsl:attribute name="name"><xsl:value-of select="@backLink"/></xsl:attribute>
            </xsl:if>
            <xsl:value-of select="@title"/>
          </a>
          <xsl:if test="$depth = 2">
            <span class="chapter-page-number"> <xsl:value-of select="@page" /> </span>
          </xsl:if>
          <xsl:if test="$depth > 2">
            <span class="section-page-number"> <xsl:value-of select="@page" /> </span>
          </xsl:if>
        </div>
      </xsl:if>
      <ul>
        <xsl:comment>added to prevent self-closing tags in QtXmlPatterns</xsl:comment>
        <xsl:apply-templates select="outline:item"/>
      </ul>
    </li>
  </xsl:template>
</xsl:stylesheet>
