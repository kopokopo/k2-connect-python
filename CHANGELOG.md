# Changelog

## 2.0.1

Drop `pip`, `wheel`, and `setuptools` from runtime dependencies.

`pip~=24.3.1` forced every install of this package onto the 24.3 line. That is below the minimum pip release (`>= 26.2.2`) recommended after the eMudhra/emSign CA incident ([discussion](https://discuss.python.org/t/information-for-python-users-regarding-emudhra-emsign-ca-certificate-security-incident/109576)). `pip` is an installer, not a library dependency. `wheel` and `setuptools` are build tools and are now declared in `[build-system].requires`.

### Affected releases

`1.2.6` and `2.0.0` publish `pip~=24.3.1` in `Requires-Dist`. Upgrade to `2.0.1`.
