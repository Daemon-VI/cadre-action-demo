# cadre-action-demo

A deliberately half-finished Python package that tests
[Cadre's GitHub Action](https://github.com/Daemon-VI/cadre) on a real repository.

`textstats` counts words, but `top_words` and `reading_time` are stubs, and their tests in
`tests/` fail. An issue labelled `cadre` asks Cadre to finish them. Cadre then posts a forecast,
runs its `project-finisher` team on free model keys, with this repository's own tests
(`.cadre/checks.yaml`) gating the work, and opens a pull request with its report and token
usage. The pull request is left for a human to merge.

```
python -m unittest discover -s tests -t .
```

Only the repository owner, members and collaborators can start a run (see
`.github/workflows/cadre.yml`). The workflow pins Cadre to a commit.
