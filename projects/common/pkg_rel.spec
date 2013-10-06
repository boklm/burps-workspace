[%-
  SET rel = 1;
  IF c('describe/tag_reach');
        rel = '0.' _ c('describe/tag_reach') _ '.g' _ c('describe/hash');
  END;
  IF c('pkg_rel');
        rel = c('pkg_rel');
  END;
-%]
