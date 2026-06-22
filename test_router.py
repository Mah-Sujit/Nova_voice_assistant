from nova_voice.core.intent_router import IntentRouter

router = IntentRouter()

print("\n=== GIT ===")
print(router.route("git status"))

print("\n=== DEBUG ===")
print(router.route("debug syntax error"))