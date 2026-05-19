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
    test:addXPBoost(Perks.Axe, 10);             -- *
    test:addXPBoost(Perks.Blunt, 10);           -- *
    test:addXPBoost(Perks.SmallBlunt, 10);      -- *
    test:addXPBoost(Perks.LongBlade, 10);       -- *
    test:addXPBoost(Perks.SmallBlade, 10);
    test:addXPBoost(Perks.Spear, 10);
    test:addXPBoost(Perks.Maintenance, 10);
    ----
    test:addXPBoost(Perks.Woodwork, 10);
    test:addXPBoost(Perks.Cooking, 10);
    test:addXPBoost(Perks.Farming, 10);         -- *
    test:addXPBoost(Perks.Doctor, 10);          -- *
    test:addXPBoost(Perks.Electricity, 10);     -- *
    test:addXPBoost(Perks.MetalWelding, 10);    -- *
    test:addXPBoost(Perks.Mechanics, 10);       -- *
    test:addXPBoost(Perks.Tailoring, 10);       -- *
    ----
    test:addXPBoost(Perks.Aiming, 10);          -- *
    test:addXPBoost(Perks.Reloading, 10);       -- *
    ----
    test:addXPBoost(Perks.Fishing, 10);
    test:addXPBoost(Perks.Trapping, 10);        -- *
    test:addXPBoost(Perks.PlantScavenging, 10);
    ----
    return test;
end

function TestTrait.OnNewGame(player)
    if not player:HasTrait("Test") then
        return
    end

    -- Asignado según el rol profesional. player:getInventory():AddItem("Base.Bag_DuffelBag");
    -- Asignado según el rol profesional. player:getInventory():AddItem("Base.HuntingKnife");
    player:getInventory():AddItem("Base.WoodAxe");
    player:getInventory():AddItem("Base.Saw");

    --[[
    player:getInventory():AddItem("Base.Sledgehammer");

    local weapon = InsurgentWeaponUtil.addWeapon(player, "Base.Shotgun", {"Base.AmmoStraps", "Base.ChokeTubeFull", "Base.RecoilPad", "Base.x2Scope"})
    InsurgentWeaponUtil.addMags(player, "Base.ShotgunShellsBox", 2)
    InsurgentWeaponUtil.equipAndFullyLoadWeapon(player, weapon, "Base.ShotgunShells")
    ]]--
end

function TestTrait.RegisterEvents()
    Events.OnNewGame.Add(TestTrait.OnNewGame)
end
```
