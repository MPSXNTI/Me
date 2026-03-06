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
