This repository uses Git LFS (Large File Storage) to track large files.

# Git LFS (Large File Storage) Guide

## What is Git LFS?

Git LFS (Large File Storage) is an open-source Git extension for versioning large files. It replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the actual file contents on a remote server.

## Why Use Git LFS?

- **Faster cloning and fetching**: Large files are downloaded only when needed
- **Reduced repository size**: Git repository stays lightweight
- **Better performance**: Git operations remain fast even with large files
- **Seamless integration**: Works transparently with Git commands

## Installation

### macOS
```bash
brew install git-lfs
```

### Linux (Debian/Ubuntu)
```bash
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
```

### Linux (RHEL/CentOS)
```bash
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | sudo bash
sudo yum install git-lfs
```

### Windows
Download installer from: https://git-lfs.github.com/

After installation, run:
```bash
git lfs install
```

## Setup in a Repository

### Initialize Git LFS in a repository
```bash
cd your-repository
git lfs install
```

### Track specific file types
```bash
# Track all .psd files
git lfs track "*.psd"

# Track all .zip files
git lfs track "*.zip"

# Track all video files
git lfs track "*.mp4"
git lfs track "*.mov"
git lfs track "*.avi"

# Track datasets
git lfs track "*.csv"
git lfs track "*.json"
```

### View tracked file types
```bash
git lfs track
```

### Untrack a file type
```bash
git lfs untrack "*.psd"
```

## Common Commands

### Add files to Git LFS
```bash
# Add specific files
git add file.psd

# Add all tracked files
git add .
```

### Check LFS status
```bash
# Show which files are tracked by LFS
git lfs ls-files

# Show LFS status
git lfs status
```

### Pull LFS files
```bash
# Pull all LFS files
git lfs pull

# Pull specific LFS files
git lfs pull --include="file.psd"
```

### Push LFS files
```bash
# Push all LFS files
git lfs push

# Push to specific remote
git lfs push origin main
```

### Fetch LFS files
```bash
# Fetch all LFS files without checking them out
git lfs fetch
```

## Workflow Example

```bash
# 1. Initialize Git LFS
git lfs install

# 2. Track file types
git lfs track "*.psd"
git lfs track "*.zip"

# 3. Commit the .gitattributes file
git add .gitattributes
git commit -m "Configure Git LFS tracking"

# 4. Add and commit large files
git add large-file.psd
git commit -m "Add large design file"

# 5. Push to remote
git push origin main
```

## Migration (Converting Existing Files)

If you already have large files in your repository:

```bash
# 1. Import existing files to LFS
git lfs migrate import --include="*.psd,*.zip,*.mp4"

# 2. Push changes
git push origin main --force
```

## Best Practices

- **Track file types, not individual files**: Use patterns like `*.psd` instead of specific filenames
- **Add .gitattributes to version control**: Always commit the `.gitattributes` file
- **Use LFS for files > 100MB**: Git LFS is most beneficial for files larger than 100MB
- **Configure Git LFS globally**: Run `git lfs install --global` to enable LFS in all repositories
- **Monitor storage usage**: Keep track of your LFS storage quota on your Git hosting service

## Troubleshooting

### Files not downloading
```bash
git lfs pull
```

### LFS not working after clone
```bash
git lfs install
git lfs pull
```

### Check LFS lock status (if using file locking)
```bash
git lfs locks
```

## Configuration

### Set default LFS storage path
```bash
git config --global lfs.storagepath /path/to/storage
```

### Set concurrent downloads
```bash
git config --global lfs.concurrenttransfers 8
```

### Disable LFS for a repository
```bash
git lfs uninstall
```

## Git Hosting Services

Git LFS is supported by:
- GitHub (Free: 1GB storage, 1GB bandwidth/month)
- GitLab (Free: 10GB storage)
- Bitbucket (Free: 1GB storage)
- Azure DevOps
- Self-hosted Git servers (requires LFS server setup)

## Resources

- Official documentation: https://git-lfs.github.com/
- GitHub LFS guide: https://docs.github.com/en/repositories/managing-large-files/about-git-large-file-storage
- GitLab LFS guide: https://docs.gitlab.com/ee/topics/git/lfs/