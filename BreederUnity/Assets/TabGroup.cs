using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TabGroup : MonoBehaviour
{
  public List<TabButton> tabButtons;
  public Color tabIdle;
  public Color tabHover;
  public Color tabActive;
  public TabButton selectedTab;
  public int currentIndex;
  public List<GameObject> objectsToSwap;

  public void Subscribe(TabButton button)
  {
    if (tabButtons == null)
    {
      tabButtons = new List<TabButton>();
    }

    tabButtons.Add(button);
    currentIndex = -1;
  }

  public void OnTabEnter(TabButton button)
  {
    ResetTabs();
    if(selectedTab == null || button != selectedTab)
    {
      button.background.color = tabHover;
    }
  }

  public void OnTabExit(TabButton button)
  {
    ResetTabs();
  }

  public void OnTabSelected(TabButton button)
  {
    int temp = currentIndex;
    currentIndex = button.transform.GetSiblingIndex();
    if(temp == currentIndex) //deselect current selection
    {
      selectedTab = null;
      currentIndex = -1;
      button.background.color = tabHover;
    } else {
      selectedTab = button;
      button.background.color = tabActive;
      objectsToSwap[currentIndex].SetActive(true);
    }
    ResetTabs();
    if (temp != -1)
    {
      objectsToSwap[temp].SetActive(false);
    }
  }

  public void ResetTabs()
  {
    foreach(TabButton button in tabButtons)
    {
      if(selectedTab != null && button == selectedTab) {continue;}
      button.background.color = tabIdle;
    }
  }
}
