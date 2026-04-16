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

<details><summary>Test</summary>

```lua

```
</details>

<details><summary>Chill</summary>

```lua
require "Insurgent/InsurgentTraitDefinitions"

ChillTrait = CreateInsurgentTrait()
ChillTrait.name = "Chill"
ChillTrait.insurgentExclusive = true

function ChillTrait.Create()
    local chill = TraitFactory.addTrait("Chill", getText("UI_trait_Chill"), 2, getText("UI_trait_ChillDesc"), false, false);
    ----
    --chill:addXPBoost(Perks.Fitness, int);	
    --chill:addXPBoost(Perks.Strength, int);
    ----
    chill:addXPBoost(Perks.Sprinting, int);
    chill:addXPBoost(Perks.Lightfoot, int);
    chill:addXPBoost(Perks.Nimble, int);
    chill:addXPBoost(Perks.Sneak, int);
    ----
    --chill:addXPBoost(Perks.Axe, int);
    --chill:addXPBoost(Perks.Blunt, int);
    --chill:addXPBoost(Perks.SmallBlunt, int);
    --chill:addXPBoost(Perks.LongBlade, int);
    chill:addXPBoost(Perks.SmallBlade, int);
    chill:addXPBoost(Perks.Spear, int);
    chill:addXPBoost(Perks.Maintenance, int);
    ----
    chill:addXPBoost(Perks.Woodwork, int);
    chill:addXPBoost(Perks.Cooking, int);
    chill:addXPBoost(Perks.Farming, int);
    --chill:addXPBoost(Perks.Doctor, int);
    --chill:addXPBoost(Perks.Electricity, int);
    --chill:addXPBoost(Perks.MetalWelding, int);
    --chill:addXPBoost(Perks.Mechanics, int);
    --chill:addXPBoost(Perks.Tailoring, int);
    ----
    --chill:addXPBoost(Perks.Aiming, int);
    --chill:addXPBoost(Perks.Reloading, int);
    ----
    chill:addXPBoost(Perks.Fishing, int);
    chill:addXPBoost(Perks.Trapping, int);
    chill:addXPBoost(Perks.PlantScavenging, int);
    ----
    return chill;
end
```
</details>
