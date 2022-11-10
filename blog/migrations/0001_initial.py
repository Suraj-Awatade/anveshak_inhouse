# Generated by Django 4.1.2 on 2022-10-18 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('year', models.IntegerField(choices=[(1600, 1600), (1601, 1601), (1602, 1602), (1603, 1603), (1604, 1604), (1605, 1605), (1606, 1606), (1607, 1607), (1608, 1608), (1609, 1609), (1610, 1610), (1611, 1611), (1612, 1612), (1613, 1613), (1614, 1614), (1615, 1615), (1616, 1616), (1617, 1617), (1618, 1618), (1619, 1619), (1620, 1620), (1621, 1621), (1622, 1622), (1623, 1623), (1624, 1624), (1625, 1625), (1626, 1626), (1627, 1627), (1628, 1628), (1629, 1629), (1630, 1630), (1631, 1631), (1632, 1632), (1633, 1633), (1634, 1634), (1635, 1635), (1636, 1636), (1637, 1637), (1638, 1638), (1639, 1639), (1640, 1640), (1641, 1641), (1642, 1642), (1643, 1643), (1644, 1644), (1645, 1645), (1646, 1646), (1647, 1647), (1648, 1648), (1649, 1649), (1650, 1650), (1651, 1651), (1652, 1652), (1653, 1653), (1654, 1654), (1655, 1655), (1656, 1656), (1657, 1657), (1658, 1658), (1659, 1659), (1660, 1660), (1661, 1661), (1662, 1662), (1663, 1663), (1664, 1664), (1665, 1665), (1666, 1666), (1667, 1667), (1668, 1668), (1669, 1669), (1670, 1670), (1671, 1671), (1672, 1672), (1673, 1673), (1674, 1674), (1675, 1675), (1676, 1676), (1677, 1677), (1678, 1678), (1679, 1679), (1680, 1680), (1681, 1681), (1682, 1682), (1683, 1683), (1684, 1684), (1685, 1685), (1686, 1686), (1687, 1687), (1688, 1688), (1689, 1689), (1690, 1690), (1691, 1691), (1692, 1692), (1693, 1693), (1694, 1694), (1695, 1695), (1696, 1696), (1697, 1697), (1698, 1698), (1699, 1699), (1700, 1700), (1701, 1701), (1702, 1702), (1703, 1703), (1704, 1704), (1705, 1705), (1706, 1706), (1707, 1707), (1708, 1708), (1709, 1709), (1710, 1710), (1711, 1711), (1712, 1712), (1713, 1713), (1714, 1714), (1715, 1715), (1716, 1716), (1717, 1717), (1718, 1718), (1719, 1719), (1720, 1720), (1721, 1721), (1722, 1722), (1723, 1723), (1724, 1724), (1725, 1725), (1726, 1726), (1727, 1727), (1728, 1728), (1729, 1729), (1730, 1730), (1731, 1731), (1732, 1732), (1733, 1733), (1734, 1734), (1735, 1735), (1736, 1736), (1737, 1737), (1738, 1738), (1739, 1739), (1740, 1740), (1741, 1741), (1742, 1742), (1743, 1743), (1744, 1744), (1745, 1745), (1746, 1746), (1747, 1747), (1748, 1748), (1749, 1749), (1750, 1750), (1751, 1751), (1752, 1752), (1753, 1753), (1754, 1754), (1755, 1755), (1756, 1756), (1757, 1757), (1758, 1758), (1759, 1759), (1760, 1760), (1761, 1761), (1762, 1762), (1763, 1763), (1764, 1764), (1765, 1765), (1766, 1766), (1767, 1767), (1768, 1768), (1769, 1769), (1770, 1770), (1771, 1771), (1772, 1772), (1773, 1773), (1774, 1774), (1775, 1775), (1776, 1776), (1777, 1777), (1778, 1778), (1779, 1779), (1780, 1780), (1781, 1781), (1782, 1782), (1783, 1783), (1784, 1784), (1785, 1785), (1786, 1786), (1787, 1787), (1788, 1788), (1789, 1789), (1790, 1790), (1791, 1791), (1792, 1792), (1793, 1793), (1794, 1794), (1795, 1795), (1796, 1796), (1797, 1797), (1798, 1798), (1799, 1799), (1800, 1800), (1801, 1801), (1802, 1802), (1803, 1803), (1804, 1804), (1805, 1805), (1806, 1806), (1807, 1807), (1808, 1808), (1809, 1809), (1810, 1810), (1811, 1811), (1812, 1812), (1813, 1813), (1814, 1814), (1815, 1815), (1816, 1816), (1817, 1817), (1818, 1818), (1819, 1819), (1820, 1820), (1821, 1821), (1822, 1822), (1823, 1823), (1824, 1824), (1825, 1825), (1826, 1826), (1827, 1827), (1828, 1828), (1829, 1829), (1830, 1830), (1831, 1831), (1832, 1832), (1833, 1833), (1834, 1834), (1835, 1835), (1836, 1836), (1837, 1837), (1838, 1838), (1839, 1839), (1840, 1840), (1841, 1841), (1842, 1842), (1843, 1843), (1844, 1844), (1845, 1845), (1846, 1846), (1847, 1847), (1848, 1848), (1849, 1849), (1850, 1850), (1851, 1851), (1852, 1852), (1853, 1853), (1854, 1854), (1855, 1855), (1856, 1856), (1857, 1857), (1858, 1858), (1859, 1859), (1860, 1860), (1861, 1861), (1862, 1862), (1863, 1863), (1864, 1864), (1865, 1865), (1866, 1866), (1867, 1867), (1868, 1868), (1869, 1869), (1870, 1870), (1871, 1871), (1872, 1872), (1873, 1873), (1874, 1874), (1875, 1875), (1876, 1876), (1877, 1877), (1878, 1878), (1879, 1879), (1880, 1880), (1881, 1881), (1882, 1882), (1883, 1883), (1884, 1884), (1885, 1885), (1886, 1886), (1887, 1887), (1888, 1888), (1889, 1889), (1890, 1890), (1891, 1891), (1892, 1892), (1893, 1893), (1894, 1894), (1895, 1895), (1896, 1896), (1897, 1897), (1898, 1898), (1899, 1899), (1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='year')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogtitle')),
            ],
        ),
    ]
