# Deployment Guide - Streamlit Cloud

## Prerequisites

- GitHub account
- Streamlit Cloud account (free at share.streamlit.io)
- Repository pushed to GitHub

## Step-by-Step Deployment

### 1. Prepare Repository

Ensure your repository has:
- ✅ `app.py` in root directory
- ✅ `requirements.txt` with all dependencies
- ✅ `.streamlit/config.toml` for theme
- ✅ All source files in `src/`, `pages/` directories
- ✅ `.gitignore` to exclude unnecessary files

### 2. Push to GitHub

```bash
# Final commit
git add .
git commit -m "feat: production ready v1.0"

# Push to GitHub
git push origin master
```

### 3. Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Select your repository: `<username>/healthai-platform`
4. Set branch: `master` (or `main`)
5. Set main file path: `app.py`
6. Click "Deploy"

### 4. Wait for Deployment

- Initial deployment takes 2-5 minutes
- Streamlit Cloud will:
  - Clone your repository
  - Install dependencies from requirements.txt
  - Start the application
  - Provide a public URL

### 5. Access Your App

Your app will be available at:
```
https://<username>-healthai-platform-app-<hash>.streamlit.app
```

Or custom domain:
```
https://healthai.streamlit.app
```

## Configuration

### Streamlit Cloud Settings

#### App Settings
- **Python version**: 3.10 (auto-detected)
- **Main file**: app.py
- **Branch**: master

#### Secrets (Optional)
If you need API keys or credentials:
1. Go to App settings → Secrets
2. Add in TOML format:
```toml
[api]
key = "your-api-key"
```

#### Advanced Settings
- **Always rerun**: Off (default)
- **Reboot app**: Available in settings menu

### Resource Limits (Free Tier)

- **RAM**: 1 GB
- **CPU**: Shared
- **Storage**: 1 GB
- **Bandwidth**: Unlimited
- **Uptime**: Apps sleep after inactivity

## Updating Your App

### Automatic Updates
Streamlit Cloud automatically redeploys when you push to GitHub:

```bash
# Make changes
git add .
git commit -m "fix: update feature"
git push origin master

# App automatically redeploys in 1-2 minutes
```

### Manual Reboot
1. Go to app dashboard
2. Click "⋮" menu
3. Select "Reboot app"

## Troubleshooting

### App Won't Start

**Check logs**:
1. Go to app dashboard
2. Click "Manage app"
3. View logs for errors

**Common issues**:
- Missing dependencies in requirements.txt
- Import errors
- File path issues (use relative paths)

### Out of Memory

**Solutions**:
1. Optimize model loading with `@st.cache_resource`
2. Limit SHAP background samples
3. Process data in batches
4. Clear unused session state

### Slow Performance

**Optimizations**:
1. Cache expensive operations
2. Use lazy imports
3. Minimize data processing
4. Optimize SHAP computations

## Custom Domain (Optional)

### Using Streamlit Cloud Domain
Free custom subdomain:
```
https://your-app-name.streamlit.app
```

Request in app settings.

### Using Your Own Domain
1. Upgrade to Streamlit Cloud Pro
2. Configure DNS CNAME record
3. Add domain in app settings

## Monitoring

### App Analytics
- View count
- User sessions
- Error rates
- Performance metrics

Access in app dashboard.

### Health Checks
Streamlit Cloud automatically monitors:
- App availability
- Response time
- Error rates

## Security

### Best Practices
1. ✅ Don't commit secrets to GitHub
2. ✅ Use Streamlit secrets for API keys
3. ✅ Validate all user inputs
4. ✅ Sanitize file uploads
5. ✅ Add rate limiting if needed

### HTTPS
All Streamlit Cloud apps use HTTPS by default.

## Backup & Recovery

### Backup Strategy
1. Keep code in GitHub (version control)
2. Export trained models separately
3. Document configuration

### Recovery
If app fails:
1. Check GitHub repository
2. Revert to last working commit
3. Redeploy from Streamlit Cloud

## Cost

### Free Tier
- ✅ Unlimited public apps
- ✅ 1 GB RAM per app
- ✅ Community support
- ✅ Automatic HTTPS

### Pro Tier ($20/month)
- More resources
- Private apps
- Custom domains
- Priority support

## Post-Deployment Checklist

- [ ] App loads without errors
- [ ] All pages accessible
- [ ] Models load correctly (if trained)
- [ ] CSV upload works
- [ ] Manual forms functional
- [ ] Error handling works
- [ ] Performance acceptable
- [ ] Mobile responsive
- [ ] Disclaimer visible
- [ ] README updated with live URL

## Sharing Your App

### Public URL
Share the Streamlit Cloud URL:
```
https://healthai.streamlit.app
```

### Embed in Website
```html
<iframe src="https://healthai.streamlit.app" 
        width="100%" height="800px">
</iframe>
```

### Social Media
Add to:
- GitHub README
- LinkedIn profile
- Portfolio website
- Twitter/X

## Maintenance

### Regular Updates
1. Update dependencies monthly
2. Retrain models quarterly
3. Monitor error logs weekly
4. Review user feedback

### Version Control
Tag releases:
```bash
git tag -a v1.0 -m "Production release"
git push origin v1.0
```

## Support

### Streamlit Community
- Forum: discuss.streamlit.io
- Docs: docs.streamlit.io
- GitHub: github.com/streamlit/streamlit

### App Issues
- Check logs first
- Review documentation
- Ask in Streamlit forum
- Open GitHub issue

---

**Deployment Status**: Ready ✅  
**Estimated Time**: 15 minutes  
**Difficulty**: Easy
