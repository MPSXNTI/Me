**Nota:** function *xTrait.Create()* limpia (cambiar todo donde salga *string* or *int*).
```lua
require "Insurgent/InsurgentTraitDefinitions"

StringTrait = CreateInsurgentTrait()
StringTrait.name = "String"
StringTrait.insurgentExclusive = true

function StringTrait.Create()
    local string = TraitFactory.addTrait("String", getText("UI_trait_String"), int, getText("UI_trait_StringDesc"), false, false);
    ----
    string:addXPBoost(Perks.Fitness, int);	
    string:addXPBoost(Perks.Strength, int);
    ----
    string:addXPBoost(Perks.Sprinting, int);
    string:addXPBoost(Perks.Lightfoot, int);
    string:addXPBoost(Perks.Nimble, int);
    string:addXPBoost(Perks.Sneak, int);
    ----
    string:addXPBoost(Perks.Axe, int);
    string:addXPBoost(Perks.Blunt, int);
    string:addXPBoost(Perks.SmallBlunt, int);
    string:addXPBoost(Perks.LongBlade, int);
    string:addXPBoost(Perks.SmallBlade, int);
    string:addXPBoost(Perks.Spear, int);
    string:addXPBoost(Perks.Maintenance, int);
    ----
    string:addXPBoost(Perks.Woodwork, int);
    string:addXPBoost(Perks.Cooking, int);
    string:addXPBoost(Perks.Farming, int);
    string:addXPBoost(Perks.Doctor, int);
    string:addXPBoost(Perks.Electricity, int);
    string:addXPBoost(Perks.MetalWelding, int);
    string:addXPBoost(Perks.Mechanics, int);
    string:addXPBoost(Perks.Tailoring, int);
    ----
    string:addXPBoost(Perks.Aiming, int);
    string:addXPBoost(Perks.Reloading, int);
    ----
    string:addXPBoost(Perks.Fishing, int);
    string:addXPBoost(Perks.Trapping, int);
    string:addXPBoost(Perks.PlantScavenging, int);
    ----
    return string;
end
```
**Nota:** Opcional si se quieren agregar armas u objetos al Trait.
```lua
function StringTrait.OnNewGame(player)
    if not player:HasTrait("String") then
        return
    end

    player:getInventory():AddItem("Base.Sledgehammer");

    local weapon = InsurgentWeaponUtil.addWeapon(player, "Base.Shotgun", {"Base.AmmoStraps", "Base.ChokeTubeFull", "Base.RecoilPad", "Base.x2Scope"})
    InsurgentWeaponUtil.addMags(player, "Base.ShotgunShellsBox", 2)
    InsurgentWeaponUtil.equipAndFullyLoadWeapon(player, weapon, "Base.ShotgunShells")
end

function StringTrait.RegisterEvents()
    Events.OnNewGame.Add(StringTrait.OnNewGame)
end
```

<details><summary>ChillTrait.lua</summary>

```lua
require "Insurgent/InsurgentTraitDefinitions"

ChillTrait = CreateInsurgentTrait()
ChillTrait.name = "Chill"
ChillTrait.insurgentExclusive = true

function ChillTrait.Create()
    local chill = TraitFactory.addTrait("Chill", getText("UI_trait_Chill"), 2, getText("UI_trait_ChillDesc"), false, false);
    ----
    chill:addXPBoost(Perks.Fitness, 10);	
    chill:addXPBoost(Perks.Strength, 10);
    ----
    chill:addXPBoost(Perks.Sprinting, 10);
    chill:addXPBoost(Perks.Lightfoot, 10);
    chill:addXPBoost(Perks.Nimble, 10);
    chill:addXPBoost(Perks.Sneak, 10);
    ----
    --chill:addXPBoost(Perks.Axe, int);
    --chill:addXPBoost(Perks.Blunt, int);
    --chill:addXPBoost(Perks.SmallBlunt, int);
    --chill:addXPBoost(Perks.LongBlade, int);
    chill:addXPBoost(Perks.SmallBlade, 10);
    chill:addXPBoost(Perks.Spear, 10);
    chill:addXPBoost(Perks.Maintenance, 10);
    ----
    chill:addXPBoost(Perks.Woodwork, 10);
    chill:addXPBoost(Perks.Cooking, 10);
    chill:addXPBoost(Perks.Farming, 10);
    --chill:addXPBoost(Perks.Doctor, int);
    --chill:addXPBoost(Perks.Electricity, int);
    --chill:addXPBoost(Perks.MetalWelding, int);
    --chill:addXPBoost(Perks.Mechanics, int);
    --chill:addXPBoost(Perks.Tailoring, int);
    ----
    --chill:addXPBoost(Perks.Aiming, int);
    --chill:addXPBoost(Perks.Reloading, int);
    ----
    chill:addXPBoost(Perks.Fishing, 10);
    --chill:addXPBoost(Perks.Trapping, int);
    chill:addXPBoost(Perks.PlantScavenging, 10);
    ----
    return chill;
end
```
</details>

<details><summary>TestTrait.lua</summary>

```lua
require "Insurgent/InsurgentTraitDefinitions"

TestTrait = CreateInsurgentTrait()
TestTrait.name = "Test"
TestTrait.insurgentExclusive = true

function TestTrait.Create()
    local test = TraitFactory.addTrait("Test", getText("UI_trait_Test"), 2, getText("UI_trait_TestDesc"), false, false);
    ----
    test:addXPBoost(Perks.Fitness, 10);	
    test:addXPBoost(Perks.Strength, 10);
    ----
    test:addXPBoost(Perks.Sprinting, 10);
    test:addXPBoost(Perks.Lightfoot, 10);
    test:addXPBoost(Perks.Nimble, 10);
    test:addXPBoost(Perks.Sneak, 10);
    ----
    test:addXPBoost(Perks.Axe, 10);
    test:addXPBoost(Perks.Blunt, 10);
    test:addXPBoost(Perks.SmallBlunt, 10);
    test:addXPBoost(Perks.LongBlade, 10);
    test:addXPBoost(Perks.SmallBlade, 10);
    test:addXPBoost(Perks.Spear, 10);
    test:addXPBoost(Perks.Maintenance, 10);
    ----
    test:addXPBoost(Perks.Woodwork, 10);
    test:addXPBoost(Perks.Cooking, 10);
    test:addXPBoost(Perks.Farming, 10);
    test:addXPBoost(Perks.Doctor, 10);
    test:addXPBoost(Perks.Electricity, 10);
    test:addXPBoost(Perks.MetalWelding, 10);
    test:addXPBoost(Perks.Mechanics, 10);
    test:addXPBoost(Perks.Tailoring, 10);
    ----
    test:addXPBoost(Perks.Aiming, 10);
    test:addXPBoost(Perks.Reloading, 10);
    ----
    test:addXPBoost(Perks.Fishing, 10);
    test:addXPBoost(Perks.Trapping, 10);
    test:addXPBoost(Perks.PlantScavenging, 10);
    ----
    return test;
end

function TestTrait.OnNewGame(player)
    if not player:HasTrait("Test") then
        return
    end

    player:getInventory():AddItem("Base.WoodAxe");
    player:getInventory():AddItem("Base.Saw");
end

function TestTrait.RegisterEvents()
    Events.OnNewGame.Add(TestTrait.OnNewGame)
end
```
</details>
