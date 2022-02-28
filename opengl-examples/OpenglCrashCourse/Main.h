#pragma once

#include "Main.g.h"

namespace winrt::OpenglCrashCourse::implementation
{
    struct Main : MainT<Main>
    {
        Main();

        int32_t MyProperty();
        void MyProperty(int32_t value);

        void ClickHandler(Windows::Foundation::IInspectable const& sender, Windows::UI::Xaml::RoutedEventArgs const& args);
    };
}

namespace winrt::OpenglCrashCourse::factory_implementation
{
    struct Main : MainT<Main, implementation::Main>
    {
    };
}
