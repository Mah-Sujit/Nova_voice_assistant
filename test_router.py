from nova_voice.core.intent_router import IntentRouter

router = IntentRouter()

print("\n=== GIT ===")
print(router.route("git status"))

print("\n=== DEBUG ===")
print(router.route("debug syntax error"))

print("\n=== TERMINAL ===")
print(router.route("list files"))

print("\n=== MODULE ERROR ===")
print(
    router.route(
        "debug ModuleNotFoundError: No module named requests"
    )
)

print("\n=== FILE ERROR ===")
print(
    router.route(
        "debug FileNotFoundError"
    )
)