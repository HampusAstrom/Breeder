using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using Breeder;

[RequireComponent(typeof(Image))]
public class TabButton : MonoBehaviour, IPointerClickHandler, IPointerEnterHandler, IPointerExitHandler
{
  public TabGroup tabGroup;
  public Image background;

  public void OnPointerClick(PointerEventData eventData)
  {
    tabGroup.OnTabSelected(this);
    World.Testrun();
  }

  public void OnPointerEnter(PointerEventData eventData)
  {
    tabGroup.OnTabEnter(this);
  }

  public void OnPointerExit(PointerEventData eventData)
  {
    tabGroup.OnTabExit(this);
  }

  void Start()
  {
    background = GetComponent<Image>();
    tabGroup.Subscribe(this);
  }

  void Update()
  {

  }
}
