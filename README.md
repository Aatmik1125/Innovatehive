# INNOVATEHIVE-REDESIGN

Redesigned prototype of InnovateHive landing page — Flask backend + Bootstrap frontend.

## Run locally

1. Create venv:
   python -m venv .venv
2. Activate:
   Windows: .venv\Scripts\activate
   mac/linux: source .venv/bin/activate
3. Install:
   pip install -r requirements.txt
4. Run:
   flask run
5. Open http://127.0.0.1:5000

## Deploy
Use Render / Railway or similar. Start command: `gunicorn app:app`

## Notes
- Contact form saves submissions to `submissions.txt` (demo).
- Replace placeholder images in `static/images/` with real assets.
- Accessibility: keyboard navigable, semantic HTML, focus outlines.
