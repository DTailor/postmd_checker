postmd_checker
==============

An app to check the package(s) status by tracking number using posta.md


How To Use:
===

  1. Install dependencies from `requirements.txt` with pip
  2. Create 'tracking_codes' file, or make a first-run for the file(it will automatically create one).
  3. Add tracking codes (1 per line) in this format `tracking_code~the_item`
  4. Run `python main.py`
  

P.S.
===

I wrote this piece for tracking items from aliexpress.com, which are send through singapore, hong-kong and china mail. Any other mail services were not tested.
