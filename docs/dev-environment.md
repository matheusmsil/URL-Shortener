# Development environment

Steps to get the same setup on another machine or in another project.

## Terminal (macOS, zsh)

- **Theme:** [Starship](https://starship.rs) with the `no-nerd-font` preset, so no special font is needed
- **Plugins:** zsh-autosuggestions, zsh-syntax-highlighting, zsh-completions

### 1. Install Homebrew

Skip this step if `brew --version` already works.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then make sure `~/.zprofile` contains this line:

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

### 2. Install the tools

```bash
brew install starship zsh-autosuggestions zsh-syntax-highlighting zsh-completions
```

### 3. Create `~/.zshrc`

If the file already exists, merge this into it instead of replacing it.

```zsh
# History (also feeds the autosuggestions)
HISTSIZE=50000
SAVEHIST=50000
setopt HIST_IGNORE_ALL_DUPS SHARE_HISTORY

# Completions (git, gh, brew and more): press Tab
if type brew &>/dev/null; then
  FPATH="$(brew --prefix)/share/zsh-completions:$(brew --prefix)/share/zsh/site-functions:$FPATH"
fi
autoload -Uz compinit
compinit
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'

# Plugins: suggestions from history, accept with the right arrow
source "$(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh"

# Theme
eval "$(starship init zsh)"

# Must stay at the end of the file
source "$(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"
```

### 4. Apply the Starship preset

```bash
mkdir -p ~/.config
starship preset no-nerd-font -o ~/.config/starship.toml
```

### 5. Open a new terminal and check it

- The prompt shows the folder and git branch.
- `git sw<Tab>` completes to `git switch`.
- Typing a previous command shows it in gray; the right arrow accepts it.

### Troubleshooting

If zsh warns about insecure directories, or Tab completion doesn't work:

```bash
chmod go-w "$(brew --prefix)/share"
rm -f ~/.zcompdump
```

Then open a new terminal.

## Git and GitHub

```bash
brew install gh
gh auth login
gh auth setup-git

git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global fetch.prune true    # remove references to deleted remote branches
git config --global pull.ff only        # stop instead of creating a surprise merge commit
```

## New project checklist

**Repository settings**
- [ ] Allow squash merging only
- [ ] Automatically delete head branches

**Ruleset on `main`**
- [ ] Block direct pushes
- [ ] Require a PR and passing CI
- [ ] Require linear history
- [ ] Skip the coverage rule and last-push approval in a solo repo with no CI yet

**Planning**
- [ ] Labels
- [ ] First milestone
- [ ] Project board: Backlog → In progress → In review → Done

**Files**
- [ ] Issue templates and PR template
- [ ] `CONTRIBUTING.md`
- [ ] `CLAUDE.md`
