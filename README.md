# autowhitebalance
auto white balance

Run:
python3 autowb.py ~/Pictures/trip

Notes
1. Gray world assumes the scene averages to neutral gray. It fails on images dominated by one color (sunsets, forests, a big blue sky). Per-channel auto-level has similar weaknesses.
2. Originals are never overwritten; results go to a corrected/ subfolder.
3. For JPEGs, both methods re-encode the file, causing a small quality loss. Use -quality 95 in ImageMagick if that matters.
4. For a one-off test, try a single image first to see whether the result looks natural before batch-processing.
