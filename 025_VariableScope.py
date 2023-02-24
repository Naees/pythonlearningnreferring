# 25. Variable Scope
# Scope =   The region that a variable is recognized
#           A variable is only available from inside the region it is created.
#           A global and locally scoped versions of a bariable can be created.

aGlobalScopeVariable = "Global"       #   global scope (available inside & outside function)

def locally_scope_variable():
    aLocalScopeVariable = "Local"    #   local scope (available only inside this function)
    return aLocalScopeVariable

print(aGlobalScopeVariable)

print(locally_scope_variable())

# Python Rule (order of use is in descending order)
#   L = Local
#   E = Enclosing
#   G = Global
#   B = Built-in
