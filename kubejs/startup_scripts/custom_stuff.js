// Custom Fluid
onEvent('fluid.registry', event => {
  // Molten Coke Brick
  event.create('molten_coke_brick').textureThick(0x292929).bucketColor(0x292929).displayName('熔融焦炉砖')

  // Molten Shadow Steel
  event.create('molten_shadow_steel').textureThick(0x4B006E).bucketColor(0x4B006E).displayName('熔融暗影钢')
})

// Custom Items
onEvent('item.registry', event => {
  event.create('boots').displayName('靴子核心')
  event.create('leggings').displayName('护腿核心')
  event.create('chestplate').displayName('胸甲核心')
  event.create('helmet').displayName('头盔核心')
  event.create('damage').displayName('伤害核心')

  event.create('chroma_ingot').displayName('色度锭')
  event.create('unassembled_chroma_ingot').displayName('半成品色度锭')
  event.create('condensed_magical_ingot').displayName('高浓度蕴魔金属锭')
  event.create('assembled_technical_ingot').displayName('高精度科技铸锭')

  event.create('elemental_essence').displayName('元素精华')
  event.create('fallen_pet').displayName('陨落宠物碎片')
  event.create('pure_evil').displayName('恶魔意志')
  event.create('condensed_mana').displayName('高浓度魔力')

  event.create('vous_verrez_en_temps_voulu').displayName('你会在适当的时候看到')
})
