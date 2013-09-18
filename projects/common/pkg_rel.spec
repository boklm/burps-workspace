[%-
  SET rel = 1;
  IF p.describe.tag_reach;
        rel = '0.' _ p.describe.tag_reach _ '.g' _ p.describe.hash;
  END;
  IF c('pkg_rel');
        rel = c('pkg_rel');
  END;
-%]
