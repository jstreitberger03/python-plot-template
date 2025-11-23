EXAMPLES = examples/line_and_scatter.py examples/muted_bar_chart.py examples/scatter_regression.py examples/stacked_area.py examples/heatmap_corr.py

.PHONY: examples lint test all

examples:
	@for f in $(EXAMPLES); do \
		echo "Running $$f"; \
		python $$f; \
	done

lint:
	ruff check .

test:
	pytest

all: lint test examples
