# Contributing to Healthcare Analytics Platform

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Environment details (OS, Python version)

### Suggesting Features

Feature requests are welcome! Please include:
- Clear description of the feature
- Use case and benefits
- Potential implementation approach
- Any relevant examples

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
   ```bash
   git commit -m "feat: add new feature"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request**

## 📝 Coding Standards

### Python Style
- Follow PEP 8 guidelines
- Use type hints
- Add docstrings to functions
- Keep functions focused and small
- Use meaningful variable names

### Code Organization
- Place new modules in `src/`
- Add tests in `tests/`
- Update documentation in `docs/`
- Keep pages in `pages/`

### Commit Messages
Use conventional commits format:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Test additions/changes
- `refactor:` - Code refactoring
- `style:` - Formatting changes
- `chore:` - Maintenance tasks

## 🧪 Testing

### Before Submitting
- Run all test suites
- Test manually in the UI
- Check for errors in console
- Verify documentation updates

### Test Commands
```bash
python tests/test_end_to_end.py
python tests/test_performance.py
python tests/test_risk_engine.py
```

## 📚 Documentation

### Update Documentation
- Add docstrings to new functions
- Update README if needed
- Add examples for new features
- Update relevant guides in `docs/`

## 🔍 Code Review

Pull requests will be reviewed for:
- Code quality and style
- Test coverage
- Documentation completeness
- Performance impact
- Security considerations

## 🚀 Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/healthai-platform.git
cd healthai-platform

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

## 📋 Areas for Contribution

### High Priority
- Additional disease modules
- Enhanced SHAP visualizations
- Performance optimizations
- Mobile responsiveness improvements

### Medium Priority
- LLM integration for recommendations
- Patient history trending
- Additional test coverage
- UI/UX enhancements

### Low Priority
- Documentation improvements
- Code refactoring
- Example notebooks
- Tutorial videos

## ❓ Questions

If you have questions:
- Check existing documentation
- Search closed issues
- Open a new issue with "Question:" prefix
- Join Streamlit community forum

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You

Your contributions help make healthcare AI more accessible and trustworthy!
