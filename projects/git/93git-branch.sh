# Include the current git branch in the prompt

if [ -f /usr/share/doc/git-core/contrib/completion/git-prompt.sh ]; then
  . /usr/share/doc/git-core/contrib/completion/git-prompt.sh
  export PS1="$(echo -n "$PS1" | sed "s|\\\W\]|\\\W\$(type __git_ps1 >/dev/null  2>\&1 \&\& __git_ps1 \" (%s)\")\]|")"
fi
