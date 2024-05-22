-- Ranks country origins of bands, ordered by
-- the number of (non-unique) fans
mysql -u root -p < metal_bands.sql;
SELECT origin, fans AS nb_fans FROM metal_bands ORDER BY nb_fans ASC;