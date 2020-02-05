namespace mdconvert
{
    /// <summary>
    /// Context in which a piece of text is to be formatted. 
    /// </summary>
    internal enum Context
    {
        Regular,
        Measure,
        Unknown,
        FrontPage,
        Title,
    }
}