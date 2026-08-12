from step_engine import get_steps

steps = get_steps("baby-dotenv", "main")
print("num steps:", len(steps))
s = steps[0]
print("title:", s.get("title"))
print("example repr:", repr(s.get("example")))
print("keys:", sorted(s.keys()))
print("annotations:", s.get("annotations"))
