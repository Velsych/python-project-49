install:
	uv sync

brain-games:
	uv run brain-games


brain-even:
	uv run brain-even


brain-calc:
	uv run brain-calc


brain-prog:
	uv run brain-progression


build:
	uv build

package-install:
	uv tool install dist/*.whl


package-reinstall: build
	uv tool install --force dist/*.whl


lint:
	uv run ruff check brain_games


fix:
	uv run ruff check brain_games --fix




