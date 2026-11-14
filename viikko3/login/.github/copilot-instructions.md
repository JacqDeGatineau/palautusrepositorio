# Copilot instructions

## Project overview

This directory contains the week 3 login exercise. It is a small Flask application
served from `src/index.py` and configured in `src/app.py`. Jinja templates under
`src/templates/` render the home, login, registration, welcome, and main pages.

The application flow is split into layers:

- Flask route handlers in `src/app.py` read form data, call the service, and
  redirect or flash an error.
- `src/services/user_service.py` owns validation, registration, and credential
  checking. `UserInputError` is used for validation failures and
  `AuthenticationError` for failed login.
- `src/repositories/user_repository.py` stores `User` objects in an in-memory
  list. The module-level `user_repository` and `user_service` instances are the
  application’s shared state, so `/tests/reset` clears state between browser
  tests.
- `src/tests/resource.robot` defines shared Browser setup, URLs, and keywords.
  The suite files use the custom `src/AppLibrary.py` library for HTTP-based
  reset and user creation, while Browser drives the UI.

The app listens on `0.0.0.0:5001` when started through `src/index.py`.

## Build, test, and run commands

Use the project directory (`viikko3/login`) as the working directory. Dependencies
are managed with `uv`; the supported Python version is declared in
`pyproject.toml` and `.python-version`.

```bash
# Install/synchronize runtime and test dependencies
uv sync

# Start the Flask server (keep this terminal running)
uv run python src/index.py

# Run all Robot Framework browser tests in another terminal
uv run robot src/tests

# Run one suite
uv run robot src/tests/login.robot

# Run one named test case
uv run robot -t "Login With Correct Credentials" src/tests/login.robot
```

The Robot suites expect the server at `http://localhost:5001`. They default to
headed Chromium (`${HEADLESS}` is `false` in `src/tests/resource.robot`); change
that variable when a headless run is needed. Browser output files such as
`output.xml`, `log.html`, and `report.html` are generated in the project root
and are ignored by Git.

## Conventions and boundaries

- Keep route functions thin: form extraction, service invocation, redirect, and
  flash handling belong in `src/app.py`; business validation belongs in
  `UserService`.
- Use the existing module-level repository/service objects so routes and the
  test reset endpoint operate on the same in-memory state. Tests should reset
  state before creating users.
- Preserve the user-facing error strings in `UserService`; Robot tests assert
  their exact text in the rendered page.
- Add browser-test setup and reusable keywords to `src/tests/resource.robot`
  rather than duplicating browser/context/URL setup in each suite.
- `AppLibrary` uses HTTP requests against the running server for test setup;
  it is not an alternative application entry point.
- `src/index.py` is the development entry point. Import `app` from `src/app.py`
  when a test or tool needs the Flask application object directly.
